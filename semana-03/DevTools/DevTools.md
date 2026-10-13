> 1. ¿Cuántos requests hace al cargar?
   Respuesta: 83 requests
> 2. Encuentra uno que devuelva JSON. Pega un pedazo.
   Respuesta:["-1", null,…]
0
: 
"-1"
1
: 
null
2
: 
[[["ANDROID_BACKUP", 0], ["BATTERY_STATS", 0], ["SMART_SETUP", 0], ["TRON", 0]], -3334737594024971300]
3
: 
[]
4
: 
{175237375: [10000]}

> 3. ¿Qué verbo y qué código de estado tiene?
    Respuesta: Método de solicitud
POST
Código de estado
200 OK
> 4. Encuentra un request que **falle** (rojo). ¿Qué código devuelve y qué significa?
    Respuesta: VM790:1 Connecting to 'https://httpstat.us/404' violates the following Content Security Policy directive: "connect-src chrome://webui-test chrome://resources chrome://theme 'self'". The action has been blocked.
    significa que no se ha encontrado los datos o no se ha enviado datos
> 5. ¿Cuánto pesa la página completa?
    Respuesta: 4,8MB