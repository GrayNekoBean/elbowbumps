<template>
    <div class="edit-button">
        <i :title="hint" class="pi edit-icon" :class="icon" :style="iconColor" @click="clickEvent"></i>
    </div>
</template>

<script>
export default {
    name: "IconButton",
    props: ["hint", "icon", "color"],
    emits: ["onClick"],
    methods: {
        clickEvent(){
            this.$emit('onClick');
        }
    },
    computed: {
        iconColor(){
            return {
                color: this.color
            };
        }
    }
}
</script>

<style lang="scss" scoped>

.edit-icon{
    height: 2rem;
    width: 2rem;
    padding: 25%;
    cursor: pointer;
}

.edit-button{
    height: 2rem;
    width: 2rem;
    :hover{
        border-radius: 50%;
        background: rgba(0, 0, 0, 0.15);
    }
}

</style>