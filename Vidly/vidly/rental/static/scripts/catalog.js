var catalog = []

function loadData(){

    $.ajax({
        url: '/api/movies',
        type: 'GET',
        success: (res) => {
            console.log('From Server', res);

            catalog = res.objects;
            for(let i=0; i < res.objects.length; i++){
                var movie = res.objects[i];
                displayMovie(movie);

            }
        },
        error: (errorDetails) => {
            console.log(errorDetails);
        }

    });
}


function displayMovie(movie){

    var tr =
    `
    <tr>
        <td><img src ='/static/images/${movie.image}'></td>
        <td><a href="/movie/${movie.id}">${movie.title}</a></td>
        <td>${movie.release_year}</td>
        <td>${movie.price}</td>
        <td>${movie.in_stock}</td>
    
    </tr>`

    $(".catalog table tbody").append(tr);
}

function init(){

    console.log("Catalog page");
    loadData();
}

window.onload = init;