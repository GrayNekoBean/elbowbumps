<template>
  <div id="text">
    <h1>CONTACT US</h1>
      <p></p>
      <p style =" color: #444444"><i>twitter:</i> <a href="https://twitter.com/elbowbumps">@elbowbumps</a></p>
      <p style =" color: #444444">Thanks for viewing our web application!</p>
      <form action="mailto:elbowbumps@outlook.com?subject=Contacting W1" target = "_blank" method="post" enctype="multipart/form-data">
        <label>Name</label> <br>
        <input type="text" name="name" placeholder="Your name"> <br>
        <label>What would you like to tell us?</label> <br>
        <textarea name="feedback" placeholder="Write something..." style="height:100px"></textarea> <br>
        <input type="submit" value="Submit">
      </form>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato&family=Open+Sans&display=swap');
$primitive-color: #a9edfe;
$secondary-color: #ffaaaa;
$background-color: 	#80929F;
//$background-color: #E95B46;
//$background-color: 	#DB744E;
//$background-color: #ffffff;
//$background-color: #fffaba;

input[type=text], select, textarea {
  width: 560%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  resize: vertical;
}

input[type=submit] {
  width: 100%;
  background-color: $secondary-color;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #ff9191;
}
#text {
  position: absolute;
  // margin: auto;
  margin-top: 5%;
  margin-left: 7%;
  margin-right: 8%;
  margin-bottom: 20%;
  font-size: 14px;
  color: #444444;
  text-align: left;
  font-family: 'Montserrat', sans-serif;;
  line-height: 25px;
  background: #ffffff;
}
div {
  border-radius: 5px;
  background-color: $background-color;
  padding: 20px;
}
</style>
