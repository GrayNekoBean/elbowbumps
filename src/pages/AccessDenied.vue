<template>
    <section>
        <div class="access_tip">
            <h2> Access Denied </h2>
            <p>You don't have access to this page currently, please <router-link to="/login">login</router-link> first.</p>
        </div>
    </section>
</template>

<style lang="scss" scoped>
.access_tip{
    position: absolute;
    display: flex;
    margin-top: 10%;
    margin-left: 35%;
    flex-flow: column;
    text-align: center;
}
</style>