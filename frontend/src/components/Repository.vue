<template>

<tr>
    <td><a :href="item.url" target="_blank">{{ item.author }}</a></td>
    <td> {{ item.stars }}</td>
    <td> {{item.created}}-{{ item.updated }}</td>
</tr>

</template>

<script>

export default {
    props: {
        item: Object
    }
};

</script>