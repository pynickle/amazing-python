function getArgs(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) {
        return unescape(r[2]);
    }
    return null;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function submit() {
    var input = document.getElementById("input").value;
    var english = document.getElementById("english").innerText;
    var choice = parseInt(getArgs("choice"));
    console.log(choice)
    if(!choice){
        choice = 0
    }
    choice += 1;
    console.log(choice);
    if (input.toUpperCase() == english.toUpperCase()) {
        document.getElementById("right").style.display = "block";
        await sleep(500);
        if(!document.getElementById("come")){
            window.location = "/recite-words?choice=" + choice.toString() + "&wrong=False";
        } else{
            window.location = "/recite-wrong-words?choice=" + choice.toString() + "&wrong=False";
        }
    } else{
        document.getElementById("wrong").style.display = "block";
        await sleep(500);
        if(!document.getElementById("come")){
            window.location = "/recite-words?choice=" + choice.toString() + "&wrong=True";
        } else{
            window.location = "/recite-wrong-words?choice=" + choice.toString() + "&wrong=True";
        }
    }
}