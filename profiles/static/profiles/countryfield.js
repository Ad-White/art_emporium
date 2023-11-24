let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', '#525252');
};
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#9EB9D4');
    } else {
        $(this).css('color', '#525252');
    }
});