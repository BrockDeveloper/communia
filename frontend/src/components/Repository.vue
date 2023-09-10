<template>
    <li>
        <a :href="item.url" target="_blank">
            {{ item.author }}
        </a>
        /
        <span> <i class="bi bi-star-fill"></i> {{ item.stars }} stelle</span>
        /
        <span> <i class="bi bi-calendar-event-fill"></i> {{ item.created }} - {{ item.updated }}</span>       
    </li>
</template>

<script>

export default {
    props: {
        item: Object
    }
};

</script>