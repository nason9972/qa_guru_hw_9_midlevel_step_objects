import os
from selene import browser, have, be



class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)
        return self


    def click_gender_male(self):
        browser.element('label[for="gender-radio-1"]').click()
        return self
    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_birth(self,month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'option[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--{day}').click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobbies(self):
        browser.element('label[for="hobbies-checkbox-1"]').click()
        return self

    def load_picture(self, file):
        browser.element('#uploadPicture').set_value(os.path.abspath(f'../test_data/{file}'))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').should(be.visible).should(be.clickable).type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(value).press_enter()
        browser.element('#submit').click()
        return self

    def should_registration_form(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.text(value))
        return self

    def should_registration_user(self, firs_name, last_name, email, male, number,birth, sub,hobbies,picture, address, state_city):
        browser.all('.table td').should(have.exact_texts(
            'Student Name', f'{firs_name} {last_name}',
            'Student Email', email,
            'Gender', male,
            'Mobile', number,
            'Date of Birth', birth,
            'Subjects', sub,
            'Hobbies', hobbies,
            'Picture', picture,
            'Address', address,
            'State and City', state_city
        ))
        return self


