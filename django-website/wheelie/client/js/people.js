$(document).ready(function() {

    var mobile;
    /* this value is set with the $large media query */
    if ($(window).width() < 1128) {
        mobile = 1;
    }

    var person = $('.people-container-person');
    var description = $('.people-container-person-description');

    var personWidth = person.width();

    if (!mobile) {
        description.css({
            'left': personWidth * 1.5
        });

        person.hover(personHover);

        function personHover() {
            var photo = $(this).find('.people-container-person-photo');
            photo.toggleClass('left');
        }
    }

    if (mobile) {
        description.click(function() {
            $(this).toggleClass('fade-in');
            description.not(this).removeClass('fade-in');
        });
    }
});