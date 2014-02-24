<script>
Array.prototype.slice.call(document.getElementsByTagName('li'))
    .forEach(function(li){
    var
    } cb = li.childNodes[0]
        cb.addEventListener('click', function(e){
            e.stopPropagation()
        })
        li.addEventListener('click', function(){
            cb.checked = !cb.checked
        }, false)
    })
</script>