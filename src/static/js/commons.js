<!-- Scripts for like question-->
$(document).ready(function () {
    $('.like_question').click(function () {
        var question_id = $(this).attr("data-question-id");
        var csrftoken = Cookies.get('csrftoken');

        $.ajax({
            url: '/like_question/',
            type: 'POST',
            data: {question_id: question_id, csrfmiddlewaretoken: csrftoken}
        }).success(function (data) {
            if (data.status == 'ok') {
                $('.question-rating').each(function () {
                    var rating_question_id = $(this).attr("data-question-id");
                    if (rating_question_id == question_id) {
                        $(this).html(data.rating);
                    }
                });
                alert(data.message);
            } else if (data.status == 'error') {
                alert(data.message);
            }
        }).error(function () {
            console.log('Error during ajax request.')
        });
    });
});

<!-- Script for like answer-->
$(document).ready(function () {
    $('.like_answer').click(function () {
        var answer_id = $(this).attr("data-answer-id");
        var csrftoken = Cookies.get('csrftoken');

        $.ajax({
            url: '/like_answer/',
            type: 'POST',
            data: {answer_id: answer_id, csrfmiddlewaretoken: csrftoken}
        }).success(function (data) {
            if (data.status == 'ok') {
                $('.answer-rating').each(function () {
                    var rating_answer_id = $(this).attr("data-answer-id");
                    if (rating_answer_id == answer_id) {
                        $(this).html(data.rating);
                    }
                });
                alert(data.message);
            } else if (data.status == 'error') {
                alert(data.message);
            }
        }).error(function () {
            console.log('Error during ajax request.')
        });
    });
});

<!-- Script for check correct answer-->
$(document).ready(function () {
    $('.answer-checkbox').change(function () {
        var check_box = $(this);
        var answer_id = $(this).attr("data-answer-id");
        var checked = !$(this).is(":checked");
        var csrftoken = Cookies.get('csrftoken');

        $.ajax({
            url: '/check_correct_answer/',
            type: 'POST',
            data: {answer_id: answer_id, checked: checked, csrfmiddlewaretoken: csrftoken}
        }).success(function (data) {
            var checked = (data.checked === "true");
            check_box.attr("checked", checked);
            alert(data.message);
        }).error(function () {
            console.log('Error during ajax request.')
        });
    });
});