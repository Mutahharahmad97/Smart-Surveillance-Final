using System;
using System.Collections.Generic;
using Thrift.Server;
using Thrift.Transport;
using System.Data.SqlClient;
using smartSurveillance;

namespace Smart_Surveillance
{
    class Server
    {
        static void Main(string[] args)
        {
            try
            {
                var handler = new APIHandler();
                var processor = new API.Processor(handler);

                TServerTransport transport = new TServerSocket(9090);
                TServer server = new TSimpleServer(processor, transport);

                Console.WriteLine("Server Started...");
                server.Serve();
            }

            catch(Exception e)  
            {
                Console.WriteLine(e.StackTrace);
            }
        }
    }

    public class APIHandler : API.Iface
    {
        public SqlConnection makeConnection()
        {
            SqlConnection conn = new SqlConnection("Data Source=MUTAHHARAHMAD97\\SQLEXPRESS;Initial Catalog=Smart Surveillance;Integrated Security=True");
            return conn;
        }

        public bool isOneAnEmployee(string name)
        {
            SqlConnection conn = makeConnection();
            conn.Open();

            SqlCommand query = new SqlCommand("select count(*) from Employee where FIRST_NAME = '"+name+"';", conn);
            int rowCount = Convert.ToInt32(query.ExecuteScalar());
            
            if(rowCount > 0)
                return true;

            return false;
        }

        public bool shouldOneBeHere(string name, string zone)
        {
            SqlConnection conn = makeConnection();
            conn.Open();

            SqlCommand query = new SqlCommand("SELECT COUNT(*) FROM DUTY_ROSTRUM DR WHERE DR.EMPLOYEE_ID IN (SELECT E.EID FROM EMPLOYEE E WHERE E.FIRST_NAME='"+name+"') AND ZONE_ID in (SELECT Z.ZID FROM ZONE Z WHERE Z.ZONE_NUMBER="+ Convert.ToInt32(zone) + ")", conn);
            int rowCount = Convert.ToInt32(query.ExecuteScalar());

            if (rowCount > 0)
                return true;

            return false;
        }

        public bool isUniformValid(string name, string uniform)
        {
            SqlConnection conn = makeConnection();
            conn.Open();

            SqlCommand query = new SqlCommand("SELECT COUNT(*) FROM DUTY_ROSTRUM DR WHERE DR.EMPLOYEE_ID IN (SELECT E.EID FROM EMPLOYEE E WHERE E.FIRST_NAME='" + name + "') AND UNIFORM_ID in (SELECT U.UID FROM UNIFORM U WHERE U.TYPE='" + uniform + "')", conn);
            int rowCount = Convert.ToInt32(query.ExecuteScalar());

            if (rowCount > 0)
                return true;

            return false;
        }

        public bool isShiftValid(string name, string datetime)
        {
            SqlConnection conn = makeConnection();
            conn.Open();

            SqlCommand query = new SqlCommand("SELECT COUNT(*) FROM DUTY_ROSTRUM DR WHERE DR.EMPLOYEE_ID IN (SELECT E.EID FROM EMPLOYEE E WHERE E.FIRST_NAME='" + name + "') AND SHIFT_ID in (SELECT S.SID FROM SHIFT S WHERE S.START_TIME < '" + datetime + "' AND S.END_TIME < '" + datetime + "')", conn);
            int rowCount = Convert.ToInt32(query.ExecuteScalar());

            if (rowCount > 0)
                return true;

            return false;
        }

        public bool isActivityIllegal(string title, string activity)
        {
            //Query
            return true;
        }

        public void reportActivity(string name, string activity)
        {
            //Query
        }
    }
}
