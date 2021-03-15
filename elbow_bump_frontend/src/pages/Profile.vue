<template>
<section>
    <Button @click="logout" style="margin: 200px;">
        Logout
    </Button>
</section>
</template>

<script>
export default {
    methods: { 
        logout: function(){
            sessionStorage.removeItem("current_user");
            localStorage.removeItem("current_user");

            this.$root.setLogoutState();

            this.$root.route_to('/');
        }
    }
}
</script>