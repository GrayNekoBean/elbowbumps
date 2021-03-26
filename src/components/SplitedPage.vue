<template>
    <div class="splited-frame">
        <div class="splited-left">
            <slot name="left"></slot>
        </div>
          
        <div class="splited-right">
            <slot name="right"></slot>
        </div>
    </div>
</template>

<style lang="scss">

$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: 	#80929F;

.splited-frame {
  position: absolute;
  height: 100%;
  width: 100%;
}

.splited-right {
  position: absolute;
  z-index: 1;
  box-shadow: 0px 0px 3px 0px;
  height: 100%;
  right: 0px;
  width: 50%;
}

.splited-left {
  position: absolute;
  z-index: 0;
  height: 100%;
  left: 0px;
  width: 50%;
  background: $primitive-color;
}

</style>