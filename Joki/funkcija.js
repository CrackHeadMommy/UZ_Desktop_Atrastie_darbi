async function jaunsJoks(){
    const atbilde = await fetch('https://api.chucknorris.io/jokes/random')
    const rezultats = await atbilde.json()
    document.getElementById("JokaVieta").innerHTML = rezultats.value
}