
document.getElementById("dark").addEventListener("click",function(event) {
   
    dark_mode_toggle()

})

if(document.getElementsByClassName("btn")[0] != null){
    for(let i=0; i<2;i++){
        document.getElementsByClassName("btn")[i].addEventListener("click",function(){
            document.getElementById("footer").classList.toggle("animate")
        })
    }
    
}

function dark_mode_toggle(){

    document.body.classList.toggle("dark")
    if(document.getElementById("select") != null){
        document.getElementById("select").classList.toggle("darkform")
    }
    if(document.getElementsByClassName("tex")[0] !=null){
        document.getElementById("search").classList.toggle("dark")
        document.getElementsByClassName("submitbutton")[0].classList.toggle("dark")
    for(let i=0; i<7;i++){
        
            document.getElementsByClassName("tex")[i].classList.toggle("darklogo")
        
    }}
    
    
}