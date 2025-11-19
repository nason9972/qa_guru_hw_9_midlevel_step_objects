from model.pages.registration_page import RegistrationPage


def test_registration_form(config_browser):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    (
        registration_page
        .fill_first_name('Иван')
        .fill_last_name('Иванов')
        .fill_user_email('ivanov@example.com')
        .click_gender_male()
        .fill_user_number('7929100500')
        .fill_date_birth("10", "1986", "025")
        .fill_subjects('Math')
        .fill_hobbies()
        .load_picture('test_image.png')
        .fill_address('Moscow, st.Lenina, 23')
        .fill_state('NCR')
        .fill_city('Delhi')
    )

    # THEN
    (registration_page
     .should_registration_form('Thanks for submitting the form')
     .should_registration_user('Иван', 'Иванов', 'ivanov@example.com', 'Male',
                               '7929100500', '25 November,1986', 'Maths', 'Sports', 'test_image.png',
                               'Moscow, st.Lenina, 23', 'NCR Delhi')
     )
