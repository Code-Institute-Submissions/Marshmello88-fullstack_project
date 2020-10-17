$("[name='more_comments']".click(function(){
    var hidden_comments = $(this).parent().find('.d-none'); // selects all hidden comments
    $(hidden_comments).each(function(){$(this).removeClass('d-none')}); // removes 'd-none' class
    })
