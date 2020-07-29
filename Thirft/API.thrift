namespace csharp smartSurveillance

service API
{
    bool isOneAnEmployee(1: string name),
    bool shouldOneBeHere(1: string name, 2: string zone),
    bool isUniformValid(1: string name, 2: string uniform),
    bool isActivityIllegal(1: string title, 2: string activity),
    bool isShiftValid(1: string name, 2: string datetime),
    void reportActivity(1:string name, 2:string activity),
}