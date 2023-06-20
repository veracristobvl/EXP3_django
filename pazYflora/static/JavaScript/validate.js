$.validator.addMethod("passwordCheck", function(password,element,parameter){
    var numeros = '0123456789'
    var caracteres_especiales = `°|¬!"#$%&/()=?¿¡´¨+*~}]{[^-:.;,`
    var  
        numero = false
        mayuscula = false, 
        minuscula = false,
        caracterEspecial = false,
        minimo = password.length >= 8 ? true : false
        
        

    
        for (let i=0; i<password.length ; i++){
            console.log('test loop ' + numeros.includes(password[i]))
            if ( numeros.includes(password[i]) )
                numero = true
            
                
            if ( caracteres_especiales.includes(password[i])) {
                caracterEspecial = true
            }

            if ( password[i] == password[i].toUpperCase() ){
                mayuscula = true
            }
            if ( password[i] == password[i].toLowerCase() ){
                minuscula = true
            }   
        }

        if (numero && mayuscula && minuscula && caracterEspecial && minimo ){
            return true
        }
        return false

},"Contraseña debe tener estructura indicada abajo")

$.validator.addMethod("passwordCheck", function(password,element,parameter){
    var numeros = '0123456789'
    var caracteres_especiales = `°|¬!"#$%&/()=?¿¡´¨+*~}]{[^-:.;,`
    var  
        numero = false
        mayuscula = false, 
        minuscula = false,
        caracterEspecial = false,
        minimo = password.length >= 8 ? true : false
        
        

    
        for (let i=0; i<password.length ; i++){
            console.log('test loop ' + numeros.includes(password[i]))
            if ( numeros.includes(password[i]) )
                numero = true
            
                
            if ( caracteres_especiales.includes(password[i])) {
                caracterEspecial = true
            }

            if ( password[i] == password[i].toUpperCase() ){
                mayuscula = true
            }
            if ( password[i] == password[i].toLowerCase() ){
                minuscula = true
            }   
        }

        if (numero && mayuscula && minuscula && caracterEspecial && minimo ){
            return true
        }
        return false

},"Contraseña debe tener estructura indicada abajo")

    
    
    
    var numeros = '0123456789'
    var caracteres_especiales = `°|¬!"#$%&/()=?¿¡´¨+*~}]{[^-:.;,`

    function passwordCheck(password){
    var  
        numero = false
        mayuscula = false, 
        minuscula = false,
        caracterEspecial = false,
        minimo = false
        
        

    
        for (let i=0; i<password.length ; i++){
            console.log('test loop ' + numeros.includes(password[i]))
            if ( numeros.includes(password[i]) )
                numero = true
            
                
            if ( caracteres_especiales.includes(password[i])) {
                caracterEspecial = true
            }

            if ( password[i] == password[i].toUpperCase() ){
                mayuscula = true
            }
            if ( password[i] == password[i].toLowerCase() ){
                minuscula = true
            }   
        }

            // numero = /^\d$/.test(password)
            //console.log(/^\d$/.test(password))
            password.length >= 8 ?
                $('#minimo-span').css({"color":"rgb(122,168,116)"}) : $('#minimo-span').css({"color":"red"})
            
            numero ? 
                $('#numero-span').css({"color":"rgb(122,168,116)"}) : $('#numero-span').css({"color":"red"})
            
            caracterEspecial ? 
                $('#car-especial-span').css({"color":"rgb(122,168,116)"}) : $('#car-especial-span').css({"color":"red"})
            mayuscula ? 
                $('#mayuscula-span').css({"color":"rgb(122,168,116)"}) : $('#mayuscula-span').css({"color":"red"})
            minuscula ? 
                $('#minuscula-span').css({"color":"rgb(122,168,116)"}) : $('#minuscula-span').css({"color":"red"})
            
}
function bordeVerde(){
    $('#test').css({"border":"3px solid rgb(122,168,116)"})
}
function fechaNacCheck(){
    var dd = $('#ffechaNac2-dd').val() || "undefined"
    
    var mm= $('#ffechaNac2-mm').val()  || "undefined"
    var yyyy= $('#ffechaNac2-yyyy').val() || "undefined"
    var fecha = dd+mm+yyyy
    fecha.includes("undefined") ? 
       $('#test').css({"border":"1px solid red "}): $('#test').css({"border":"1px solid rgb(122,168,116)"}) 
            
}
$().ready(function(){
    
    $("#formulario-validate").validate({
        rules: {
            fnombre : "required",
            fapellido : "required",
            femail : {
                required : true,
                email : true
            },
            fpassword : {
                required: true,
                minlength : 8,
                passwordCheck : ''
            },
            fpassword2 : {
                required: true,
                minlength : 8,
                equalTo : "#fpassword"
            }
        },
        messages : {
            fnombre : "Porfavor ingrese su nombre",
            fapellido : "Porfavor ingrese su apellido ",
            femail : {
                required : "Porfavor ingrese su email",
                email : "Formato de email incorrecto"
            },
            fpassword : {
                required: "Porfavor ingresa la contraseña",
                minlength : "Contraseña debe tener al menos 8 caracteres"
            },
            fpassword2 : {
                required: "Porfavor re ingresa la contraseña",
                minlength : "Contraseña debe tener al menos 8 caracteres",
                equalTo : "Contraseña debe ser igual a la contraseña ingresada anteriormente"
            },
            ffechaNac2: {
                required: ""
            }
        }
    })

    
    
   
});
