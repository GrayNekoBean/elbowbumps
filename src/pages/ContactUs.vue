<template>
  <div>Contact us!</div>
  <div id="text">
    <h1>CONTACT US</h1>
      <p></p>
      <p style =" color: #444444"><i>twitter:</i> <a href="https://twitter.com/elbowbumps">@elbowbumps</a></p>
      <p style =" color: #444444">Thanks for viewing our web application!</p>

      <form action="mailto:elbowbumps@elbowbumps.com? subject=Contacting W1" method="post" enctype="text/plain">
        <label>First Name</label> <br>
        <input type="text" name="firstname" placeholder="Your name"> <br>

        <label>Email Address</label> <br>
        <input type="text" name="email" placeholder="Your email address"> <br>

        <label>What would you like to tell us?</label> <br>
        <textarea name="experience" placeholder="Write something..." style="height:100px"></textarea> <br>
        <input type="submit" value="Submit"/>
      </form>

  </div>

</template>

<script>
export default {};
</script>

<style></style>
