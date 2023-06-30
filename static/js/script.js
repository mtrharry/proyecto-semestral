
window.addEventListener('load', () => {


    let lon
    let lat

    let temperaturaValor = document.getElementById('temperatura-valor')  
    let temperaturaDescripcion = document.getElementById('temperatura-descripcion')  
    
    let ubicacion = document.getElementById('ubicacion')  
    let iconoAnimado = document.getElementById('icono-animado') 

    let vientoVelocidad = document.getElementById('viento-velocidad') 
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(posicion => {
            console.log(posicion)

            lon = posicion.coords.longitude
            lat = posicion.coords.latitude
            const url = `https://api.openweathermap.org/data/2.5/weather?&lang=es&lat=${lat}&lon=${lon}&appid=1d19a88a0ed188f82a8212ec59d71032`

            console.log(url)

            fetch(url)
            .then( response => { return response.json() })
            .then( data => {
                
                
                let temp = Math.round(data.main.temp - 273)
                temperaturaValor.textContent = temp + ' C'
                console.log(data)
                let desc = data.weather[0].description
                temperaturaDescripcion.textContent = desc.toUpperCase()
                ubicacion.textContent = data.name
                
                vientoVelocidad.textContent = `${data.wind.speed} m/s`
                
                var iconoAnimado = document.getElementById("icono-animado");
                var staticPath = iconoAnimado.getAttribute("data-static-path");
                
                console.log(data.weather[0].main)
                switch (data.weather[0].main) {
                  case 'Thunderstorm':
                      iconoAnimado.src = staticPath + "thunder.svg";
                      console.log('TORMENTA');
                      break;
                  case 'Drizzle':
                      iconoAnimado.src = staticPath + "rainy-2.svg";
                      console.log('LLOVIZNA');
                      break;
                  case 'Rain':
                      iconoAnimado.src = staticPath + "rainy-7.svg";
                      console.log('LLUVIA');
                      break;
                  case 'Snow':
                      iconoAnimado.src = staticPath + "snowy-6.svg";
                      console.log('NIEVE');
                      break;
                  case 'Clear':
                      iconoAnimado.src = staticPath + "day.svg";
                      console.log('LIMPIO');
                      break;
                  case 'Atmosphere':
                      iconoAnimado.src = staticPath + "weather.svg";
                      console.log('ATMOSFERA');
                      break;
                  case 'Clouds':
                      iconoAnimado.src = staticPath + "cloudy-day-1.svg";
                      console.log('NUBES');
                      break;
                  default:
                      iconoAnimado.src = staticPath + "cloudy-day-1.svg";
                      console.log('por defecto');
              }

            })
            .catch(error =>{
                console.log(error)


            })
        })
    }
})
