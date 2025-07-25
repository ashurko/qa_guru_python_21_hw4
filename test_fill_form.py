import os
from selene import browser, be, have


def test_fill_form():
    browser.element('[id="firstName"]').type("Anton")
    browser.element('[id="lastName"]').type("Shurko")
    browser.element('[id="userEmail"]').type("antonshurko@gmail.com")
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type("9159379992")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="10"]').should(be.visible).click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1995"]').should(be.visible).click()
    browser.element('.react-datepicker__day--022').click()
    #browser.element('[id="dateOfBirthInput"]').set(1995/11/22).press_enter()
    browser.element('#subjectsInput').type("English").press_enter()
    browser.element('label[for ="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_file.txt'))
    browser.element('#currentAddress').type('Some address')
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()

    browser.element('[id = "example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))

#дополнительно попробовал добавить проверок на правильность отображаемых данных
    browser.element('[class = "modal-content"]').should(be.visible)
    browser.element('.table').should(have.text('Anton'))
    browser.element('.table').should(have.text('Shurko'))
    browser.element('.table').should(have.text('antonshurko@gmail.com'))
    browser.element('.table').should(have.text('9159379992'))
    browser.element('.table').should(have.text('22 November,1995'))
    browser.element('.table').should(have.text('English'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('Some address'))
    browser.element('.table').should(have.text('NCR Delhi'))
    browser.element('.table').should(have.text('test_file.txt'))