<template>
    <div  id="container">
        <img src="../assets/logingif.gif" alt="friendly GIF" id="gif">
        <h2 id="caption">Wishing you had a friend this good? <br> Don't worry we at <span style = "color: #a9edfe">ELBOW</span> <span style = "color: #ffaaaa">BUMPS</span> have you covered.</h2>
    </div>
</template>

<style lang="scss" scoped>
#container {
    background: #ffffff;
}
#gif {
    position: absolute;
    display: block;
    top: 60%;
    -ms-transform: translateY(-60%);
    transform: translateY(-60%);
    padding: 1rem 1rem 1rem 1rem;
    margin-left: 10rem;
    height: auto;
    width: 75%;
}
#caption {
    position: absolute;
    padding: 1rem 1rem 1rem 1rem;
    margin: 15rem 11rem;
    text-align: right;
    height: 5rem;
    width: 72%;
    justify-content: center;
    background: #80929F;
    color: #ffffff;
}
</style>