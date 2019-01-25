<template>
<div class="patient">
  <div>
    <img src="https://www.finearttips.com/wp-content/uploads/2010/05/avatar.jpg"/>
    <h3>Naam: <span>{{ patient.fullname }}</span> </h3>
    <p>Leeftijd: <span>{{ patient.leeftijd }}</span></p>
    <p>Initiele doses: <span>{{ patient.initialdoses }}</span> </p>
    <p>BodyMass: <span>{{ patient.bodymass}}</span> </p>
  </div>
</div>
</template>

<script>
export default {
  name: 'Patient',
  props: ['patient']
}
</script>


bodymass:16
created:"Wed, 23 Jan 2019 00:00:00 GMT"
fullname:"Juliet Manrho"
id:1
initialdoses:"10.3mg Levodopa"
leeftijd:20
