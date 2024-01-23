from fastapi import FastAPI

app = FastAPI()

@app.get("/domain_info/{domain_name}")
async def read_domain_info(domain_name: str):
    import whois
    import datetime

    w = whois.whois(domain_name)

    # Get the first element if it's a list, else use the value
    creation_date = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
    expiration_date = w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date
    updated_date = w.updated_date[0] if isinstance(w.updated_date, list) else w.updated_date
    domain_name_value = w.domain_name[0] if isinstance(w.domain_name, list) else w.domain_name
    name_servers = w.name_servers[0] if isinstance(w.name_servers, list) else w.name_servers

    # Calculate days until expiration
    days_until_expiration = (expiration_date - datetime.datetime.now()).days

    # Create a dictionary to store values
    result_dict = {
        "Creation Date": creation_date,
        "Expiration Date": expiration_date,
        "Updated Date": updated_date,
        "Domain Name": domain_name_value,
        "Name Servers": name_servers,
        "Expiry Date By Day": days_until_expiration
    }

    return result_dict