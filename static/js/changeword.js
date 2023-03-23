

var words = new Array( ' HTML',
          ' CSS',
          ' JAVASCRIPT',
          'REACTJS',
          ' PYTHON',
          'MYSQL',
          'DJANGO');


var i = 0;
setInterval( function(){
    $( '#changingword' ).empty().append( words[ i ] );
    if( i < words.length ) {
        i++;
    } else {
        i = 0;
    }
}, 2000 );