# Datos simulados para la tabla customers
customers_data = [
    {"id": 1, "first_name": "Whitney", "last_name": "Ferrero"},
    {"id": 2, "first_name": "Dickie", "last_name": "Romera"}
]

# Datos simulados para la tabla campaigns
campaigns_data = [
    {"id": 1, "customer_id": 1, "name": "Upton Group"},
    {"id": 2, "customer_id": 1, "name": "Roob, Hudson and Rippin"},
    {"id": 3, "customer_id": 1, "name": "McCullough, Rempel and Larson"},
    {"id": 4, "customer_id": 1, "name": "Lang and Sons"},
    {"id": 5, "customer_id": 2, "name": "Ruecker, Hand and Haley"}
]

# Datos simulados para la tabla events
events_data = [
    {"dt": "2021-12-02 13:52:00", "campaign_id": 1, "status": "failure"},
    {"dt": "2021-12-02 08:17:48", "campaign_id": 2, "status": "failure"},
    {"dt": "2021-12-02 08:18:17", "campaign_id": 2, "status": "failure"},
    {"dt": "2021-12-01 11:55:32", "campaign_id": 3, "status": "failure"},
    {"dt": "2021-12-01 06:53:16", "campaign_id": 4, "status": "failure"},
    {"dt": "2021-12-02 04:51:09", "campaign_id": 4, "status": "failure"},
    {"dt": "2021-12-01 06:34:04", "campaign_id": 5, "status": "failure"},
    {"dt": "2021-12-02 03:21:18", "campaign_id": 5, "status": "failure"},
    {"dt": "2021-12-01 03:18:24", "campaign_id": 5, "status": "failure"},
    {"dt": "2021-12-02 15:32:37", "campaign_id": 1, "status": "success"},
    {"dt": "2021-12-01 04:23:20", "campaign_id": 1, "status": "success"},
    {"dt": "2021-12-02 06:53:24", "campaign_id": 1, "status": "success"},
    {"dt": "2021-12-02 08:01:02", "campaign_id": 2, "status": "success"},
    {"dt": "2021-12-01 15:57:19", "campaign_id": 2, "status": "success"},
    {"dt": "2021-12-02 16:14:34", "campaign_id": 3, "status": "success"},
    {"dt": "2021-12-02 21:56:38", "campaign_id": 3, "status": "success"},
    {"dt": "2021-12-01 05:54:43", "campaign_id": 4, "status": "success"},
    {"dt": "2021-12-02 17:56:45", "campaign_id": 4, "status": "success"},
    {"dt": "2021-12-02 11:56:50", "campaign_id": 4, "status": "success"},
    {"dt": "2021-12-02 06:08:20", "campaign_id": 5, "status": "success"}
]

# Función para obtener el nombre completo del cliente
def get_full_name(customer_id):
    for customer in customers_data:
        if customer["id"] == customer_id:
            return f"{customer['first_name']} {customer['last_name']}"
    return None

# Contador de eventos de falla para cada cliente
failure_count = {}

# Contar eventos de falla para cada cliente
for event in events_data:
    campaign_id = event["campaign_id"]
    customer_id = next(campaign["customer_id"] for campaign in campaigns_data if campaign["id"] == campaign_id)
    if event["status"] == "failure":
        if customer_id in failure_count:
            failure_count[customer_id] += 1
        else:
            failure_count[customer_id] = 1

# Filtrar clientes con más de 3 eventos de falla y mostrar resultados
print("customer", "failures")
for customer_id, count in failure_count.items():
    if count > 3:
        customer_name = get_full_name(customer_id)
        print(customer_name, count)
