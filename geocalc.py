from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None
    erro = None

    if request.method == "POST":
        try:
            latitude = float(request.form["latitude"].replace(",", "."))
            longitude = float(request.form["longitude"].replace(",", "."))

            if not -90 <= latitude <= 90:
                raise ValueError("Latitude deve estar entre -90 e 90.")

            if not -180 <= longitude <= 180:
                raise ValueError("Longitude deve estar entre -180 e 180.")

            if latitude < 0:
                hemisferio = "Sul"
            elif latitude > 0:
                hemisferio = "Norte"
            else:
                hemisferio = "Linha do Equador"

            if longitude < 0:
                posicao = "Oeste"
            elif longitude > 0:
                posicao = "Leste"
            else:
                posicao = "Meridiano de Greenwich"

            # Cálculo básico da zona UTM
            if longitude == 180:
                zona_utm = 60
            else:
                zona_utm = int((longitude + 180) / 6) + 1

            resultado = {
                "latitude": latitude,
                "longitude": longitude,
                "hemisferio": hemisferio,
                "posicao": posicao,
                "zona": zona_utm
            }

        except ValueError as e:
            erro = str(e)

        except Exception:
            erro = "Digite coordenadas válidas."

    return render_template(
        "index.html",
        resultado=resultado,
        erro=erro
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
