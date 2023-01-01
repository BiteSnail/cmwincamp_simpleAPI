fetch("http://127.0.0.1:8000/names")
.then((response)=> {
    return response.json()
})
.catch((error)=>{
    console.log(error)
})
.then((data)=>{
    list = data.names
    for (idx in list){
        const obj = document.createElement("div")
        obj.className = "item"
        obj.innerHTML = list[idx]
        document.getElementById("namelist").appendChild(obj)
    }
})

async function onButtonClick(){
    const nameInput = document.getElementById('name');
    
    await fetch("http://127.0.0.1:8000/birth", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username: nameInput.value
        })
    })
    .then((response)=>{
        return response.json()
    })
    .catch((error)=> {
        console.log(error)
    })
    .then((data)=>{
        if(data.birthday === null){

            return;
        }
        const birth = new Date(data.birthday)
        const innerStr = data.username + 
                        "님의 생일은" +
                        birth.getFullYear() + "년" +
                        (birth.getMonth() + 1) + "월" +
                        birth.getDate() + "일 입니다."
        const birthStr = document.getElementById("datelist");
        birthStr.innerHTML = innerStr;
    })
}