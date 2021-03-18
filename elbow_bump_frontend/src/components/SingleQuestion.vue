<template>
        <div class="question-div">
            <div class="question-paragraph">
                <slot>This is an empty question, please enter something here.</slot>
            </div>
            <div v-for="i in marks" :key="i">
                <RadioButton class="question-selection" :name="i" :value="i" v-model="select" />
                <label>{{ i }}</label>
            </div>
        </div>
</template>

<script>
export default {
    watch: {
        select: function(val){
            this.$emit('selected', Number(val));
            //this.$props.selected = val;
            //console.log(this.selected);
        }
    },
    emits: [
        'selected'
    ],
    data() {
        return {
            marks: [1, 2, 3, 4, 5],
            select: -1
        }
    }
}
</script>

<style lang="scss" scoped>

.question-div {
    //position: absolute;
    display: flex;
    flex-wrap: nowrap;
    flex-direction: row;
    align-items: center;
    text-align: center;
    justify-content: space-between;
    margin-top: 3rem;
    width: 90%;
}

.selections-div {
    position: absolute;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: center;
    justify-content: center;
}

.question-paragraph{
    width: 30%;
    text-align: left;
}

.question-selection{
    margin-left: 6%;
}

</style>