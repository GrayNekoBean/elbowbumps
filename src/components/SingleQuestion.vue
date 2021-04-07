<template>
        <div class="question-div">
            <div class="question-paragraph">
                <slot>This is an empty question, please enter something here.</slot>
            </div>
            <div v-for="i in marks" :key="i">
                <RadioButton class="question-selection" :name="i" :value="i" v-model="select"  />
                <div class="tooltip"><label> <b> {{ i }} </b> </label>
                    <span class="tooltiptext">{{ scale[i-1] }}</span>
                </div>
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
            select: -1,
            scale: ["Strongly Agree","Agree","No opinion", "Disagree", "Strongly Disagree"]
        }
    }
}
</script>

<style lang="scss" scoped>

.tooltip {
  position: relative;
  display: inline-block;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: #7da9b4;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -60px;
  opacity: 0;
  transition: opacity 0.3s;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}




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