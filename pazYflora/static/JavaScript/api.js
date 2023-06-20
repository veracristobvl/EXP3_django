$().ready(function(){
    let url='http://localhost:3000/productos';

        const mostrarData=(data)=>{
            console.log(data)
            let body=""
            for(var i=0; i<data.length; i++){
                body+=` 
                    <div class="col-lg-3 col-12 col-md-6" style="margin-bottom: 1rem;">
                        <div class="card h-100" style="width: auto;">
                            <img class="card-img-top" src="${data[i].imgURL}" alt="Card image cap">
                            <div class="card-body">
                                <h5 class="card-title">${data[i].title}</h5>
                                <p class="card-text">${data[i].descripcion}</p>
                                <p class="card-text">$${data[i].precio}</p>
                                <a href="#" class="btn btn-primary">Agregar al Carro</a>
                            </div>
                        </div>
                    </div>`
            }
            document.getElementById('productos-row').innerHTML=body
        }
        
        fetch(url)
            .then(response => response.json())
            .then(data => mostrarData(data))
            .catch(error=>console.log(error))

       


            fetch('http://localhost:3000/usuarios', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(usuario)
                })
                .then(response => response.json())
                .then(response => console.log(JSON.stringify(response)))


               
    
})