# TODO

# Spec-Sim API
## USER
### POST /api/user/:sessionID

**Purpose**: Checks if the user   

**Place**: Registration page

**Request body:**
```
{
  "organizationName": "google", 
  "email": "joe@brosef.com",
  "password": "correct-horse-battery-staple"
}
```

**Response body:** 
```
  {
    "organizationName": "Elon Musk's Mighty Devils",
    "password": "$2a$10$uN2lH0tpxKbsVVejH2Ft/enGw87FOjUc6bDzThQ56PV2Ln1TtjO1W",
    "email": "muskyhusk@tesla.com",
    "twilio": {
        "sid": "AC301ed9287eaf02c492252079afb2e4dc",
        "authToken": "936452ece6fca5bfeb20f24ce74a61f1",
        "accountFriendlyName": "Elon Musk's Mighty Devils",
        "dateCreated": "2019-01-17T17:04:15.000Z",
        "dateUpdated": "2019-01-17T17:04:15.000Z",
        "status": "active",
        "phones": []
    }
}