---
config:
  layout: elk
---
sequenceDiagram
    participant Driver
    participant MobileApp as Mobile App
    participant ChargingStation as Charging Station
    participant BackendCMS as Backend/CMS
    participant GridEMS as Grid/EMS

    Driver->>MobileApp: Open app / Request nearby stations
    MobileApp->>MobileApp: Get user location (GPS)
    MobileApp->>BackendCMS: Send location (lat, long)
    BackendCMS->>BackendCMS: Fetch nearby stations
    BackendCMS->>BackendCMS: Check real-time availability
    BackendCMS-->>MobileApp: Return stations + availability data
    MobileApp-->>Driver: Display nearby stations on map/list

    Driver->>MobileApp: Select station & plug in vehicle
    MobileApp->>ChargingStation: Plug in vehicle
    ChargingStation->>ChargingStation: Detect connection
    MobileApp->>ChargingStation: Initiate authentication
    ChargingStation->>BackendCMS: Send auth request
    BackendCMS-->>ChargingStation: Auth success
    ChargingStation-->>MobileApp: Auth success

    MobileApp->>ChargingStation: Send start charging request
    ChargingStation->>BackendCMS: OCPP StartTransaction.req
    BackendCMS->>GridEMS: Fetch grid conditions
    GridEMS->>GridEMS: Evaluate user preferences + tariffs
    GridEMS->>GridEMS: Decide optimal charging rate
    GridEMS-->>BackendCMS: OCPP SetChargingProfile.req (rate)
    BackendCMS->>ChargingStation: Apply charging profile
    ChargingStation->>ChargingStation: Apply charging profile

    ChargingStation-->>MobileApp: Begin charging
    MobileApp-->>Driver: Begin charging

    loop Charging session
        ChargingStation->>BackendCMS: OCPP MeterValues.req (status updates)
        BackendCMS-->>MobileApp: Push updates (status, cost, battery)
        MobileApp-->>Driver: View charging status
    end