import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="vusionapiwebhook")
def vusionapiwebhook(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Webhook recibido.')
    try:
        req_body = req.get_json()
        logging.info(f"Mensaje recibido: {req_body}")
    except ValueError:
        return func.HttpResponse(
            "Cuerpo del mensaje no es válido.",
            status_code=400
        )

    return func.HttpResponse(
        "OK",
        status_code=200
    )