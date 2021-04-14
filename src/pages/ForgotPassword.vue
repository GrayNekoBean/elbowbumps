<template>
  <div>
    <div class="heading">
      <h2>Seems like you forgot your password...</h2>
    </div>

    <div id="creds">
      <form method="POST" action="alert('Reset link sent! Check your inbox.')">
        <label>Email:</label>
        <input type="email" name="email" id="email" required /><br />
        <button type="submit">Submit</button><br />
      </form>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
