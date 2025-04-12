<template>
    <div class="column" id="column1" onclick="expandColumn('column1')">
        <div class="column-content">Column 1</div>
    </div>
    <div class="column" id="column2" onclick="expandColumn('column2')">
        <div class="column-content">Column 2</div>
    </div>
    <div class="column" id="column3" onclick="expandColumn('column3')">
        <div class="column-content">Column 3</div>
    </div>

</template>
<script>
function expandColumn(columnId) {
    document.querySelectorAll('.column').forEach(column => {
        column.classList.remove('expanded');
    });
    document.getElementById(columnId).classList.add('expanded');
}
</script>


<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    display: flex;
    height: 100vh;
}

.column {
    flex: 1;
    transition: flex 0.3s ease;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #ccc;
}

.column.expanded {
    flex: 3;
}

.column-content {
    padding: 20px;
    text-align: center;
}
</style>