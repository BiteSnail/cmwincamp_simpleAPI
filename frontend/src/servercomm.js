const getData = () => {
    fetch("http://127.0.0.1:8000/names")
    .then((response)=> {
        return response.json()
    })
    .then((data)=>{
        const namelist = document.getElementById("namelist")
        list = data.names
        namelist.innerHTML = ""
        for (idx in list){
            const obj = document.createElement("div");
            obj.id = "name"+ idx;
            obj.className = "item";
            obj.onclick = function() {onButtonClick(obj.id); };
            obj.innerHTML = list[idx];
            namelist.appendChild(obj);
        }
    })
    .catch((error)=>{
        console.log(error)
    })
}

async function onButtonClick(id){
    const nameInput = document.getElementById(id);
    await fetch("http://127.0.0.1:8000/birth", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username: nameInput.innerHTML
        })
    })
    .then((response)=>{
        return response.json()
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
    .catch((error)=> {
        console.log(error)
    })
}

async function onButtonClick2(){
    const nameInput = document.getElementById('name');
    const birthInput = document.getElementById('birth');

    await fetch("http://127.0.0.1:8000/create", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username: nameInput.value,
            birthday: birthInput.value
        })
    })
    .then((response)=>{
        getData()
    })
    .catch((error)=>{
        console.log(error);
    })
}