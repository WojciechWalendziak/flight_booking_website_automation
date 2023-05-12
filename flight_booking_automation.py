import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

counter = 0
searched_month = 0
first_departure_month = 0
searched_year = 0
first_departure_years = 0
searched_day = 0
first_departure_day = 0
searched_month = 0
second_departure_month = 0
searched_year = 0
second_departure_years = 0
searched_day = 0
second_departure_day = 0
df = pd.read_excel('travel_plans.xlsx', sheet_name='Arkusz1')
number_list = df['number'].tolist()
my_class_list = df['seat class'].tolist()
first_departure_location_list = df['first departure location'].tolist()
first_arrival_location_list = df['first arrival location'].tolist()
second_departure_location_list = df['second departure location'].tolist()
final_destination_location_list = df['final destination location'].tolist()
first_departure_month_list = df['first departure month'].tolist()
first_departure_years_list = df['first departure year'].tolist()
first_departure_day_list = df['first departure day'].tolist()
second_departure_month_list = df['second departure month'].tolist()
second_departure_years_list = df['second departure year'].tolist()
second_departure_day_list = df['second departure day'].tolist()
adults_amount_list = df['adults amount'].tolist()
youth_amount_list = df['youth amount'].tolist()
child_amount_list = df['child amount'].tolist()
baby_amount_list = df['baby amount'].tolist()

for number in number_list:

    my_class = my_class_list[counter]
    first_departure_location = first_departure_location_list[counter]
    first_arrival_location = first_arrival_location_list[counter]
    second_departure_location = second_departure_location_list[counter]
    final_destination_location = final_destination_location_list[counter]
    first_departure_month = first_departure_month_list[counter]
    first_departure_years = first_departure_years_list[counter]
    first_departure_day = first_departure_day_list[counter]
    second_departure_month = second_departure_month_list[counter]
    second_departure_years = second_departure_years_list[counter]
    second_departure_day = second_departure_day_list[counter]
    adults_amount = adults_amount_list[counter]
    youth_amount = youth_amount_list[counter]
    child_amount = child_amount_list[counter]
    baby_amount = baby_amount_list[counter]

    driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(3)

    try:
        driver.get('https://www.esky.pl/tanie-loty?gclid=EAIaIQobChMIx4jzwvnU_gIVyAqiAx0M9ATbEAAYAiAAEgKxNPD_BwE')
        time.sleep(5)
    except:
        print('page loading failed')

    try:
        cookie_box = driver.find_element(By.ID, 'CybotCookiebotDialog')
        cookie_button = cookie_box.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
        cookie_button.click()
        time.sleep(3)
    except:
        print('cookie window not found')

    try:
        outer_form_box = driver.find_element(By.ID, 'multiQsfFlights')
        form_box = outer_form_box.find_element(By.TAG_NAME, 'form')
    except:
        print('form box not found')

    try:
        form_top = form_box.find_element(By.CLASS_NAME, 'top')
        main_class = form_box.find_element(By.CLASS_NAME, 'main')
    except:
        print('top & main class not found')

    try:
        trip_type_list = Select(form_top.find_element(By.ID, 'serviceClass'))
    except:
        print('class selector not found')

    try:
        trip_type_list.select_by_value(my_class)
        time.sleep(5)
    except:
        print('selecting ' + str(my_class) + ' option from dropdown failed')
    try:
        trip_type_list = form_top.find_element(By.CLASS_NAME, 'trip-type-list')
    except:
        print('trip_type_list class not found')

    try:
        li_tags = trip_type_list.find_elements(By.TAG_NAME, 'li')
        for li_tag in li_tags:
            try:
                demanded_li = li_tag.find_element(By.ID, 'TripTypeMulticity')
                demanded_li.click()
                time.sleep(3)
            except:
                continue
    except:
        print('travel type not selected')

    try:
        tm = main_class.find_element(By.ID, 'tm')
    except:
        print('tm block not found')

    try:
        departure_location_0 = tm.find_element(By.ID, 'departureMulticity0')
        departure_location_0.send_keys(first_departure_location)
        arrival_location_0 = tm.find_element(By.ID, 'arrivalMulticity0')
        arrival_location_0.send_keys(first_arrival_location)
        departure_location_1 = tm.find_element(By.ID, 'departureMulticity1')
        departure_location_1.send_keys(second_departure_location)
        arrival_location_1 = tm.find_element(By.ID, 'arrivalMulticity1')
        arrival_location_1.send_keys(final_destination_location)
    except:
        print('arrivals and/or departures locations not found')

    try:
        departure_dates = tm.find_elements(By.CLASS_NAME, 'trip-dates')
    except:
        print('trip-dates not found')
    count = 0
    for departure_date in departure_dates:
        try:
            date_button = departure_date.find_element(By.TAG_NAME, 'button')
            date_button.click()
            time.sleep(3)
            check = 1
            count = count + 1
        except:
            check = 0

        if check == 1:
            check = 0
            if count < 2:
                searched_month = first_departure_month
                searched_year = first_departure_years
                searched_day = first_departure_day
            else:
                searched_month = second_departure_month
                searched_year = second_departure_years
                searched_day = second_departure_day
            count = count + 1
            while check == 0:
                try:
                    date_selection_box = driver.find_element(By.ID, 'ui-datepicker-div')
                except:
                    print('ui-datepicker-div not found')
                try:
                    date_selection_box_header = date_selection_box.find_element(By.CLASS_NAME, 'ui-datepicker-header')
                except:
                    print('ui - datepicker - header not found')
                try:
                    move_to_next_month_button = date_selection_box_header.find_element(By.CLASS_NAME, 'ui-datepicker-next')
                except:
                    print('ui-datepicker-next not found')
                try:
                    current_month_and_year_box = date_selection_box_header.find_element(By.CLASS_NAME, 'ui-datepicker-title')
                except:
                    print('ui-datepicker-title not found')
                try:
                    current_month = current_month_and_year_box.find_element(By.CLASS_NAME, 'ui-datepicker-month')
                    current_month = current_month.get_attribute('innerHTML').strip()
                except:
                    print('ui-datepicker-month not found')
                try:
                    current_year = current_month_and_year_box.find_element(By.CLASS_NAME, 'ui-datepicker-year')
                    current_year = current_year.get_attribute('innerHTML').strip()
                except:
                    print('ui-datepicker-year not found')

                if str(current_month) == str(searched_month) and str(current_year) == str(searched_year):
                    check = 1
                    match searched_month:
                        case 'Styczeń':
                            int_searched_month = 1
                        case 'Luty':
                            int_searched_month = 2
                        case 'Marzec':
                            int_searched_month = 3
                        case 'Kwiecień':
                            int_searched_month = 4
                        case 'Maj':
                            int_searched_month = 5
                        case 'Czerwiec':
                            int_searched_month = 6
                        case 'Lipiec':
                            int_searched_month = 7
                        case 'Sierpień':
                            int_searched_month = 8
                        case 'Wrzesień':
                            int_searched_month = 9
                        case 'Październik':
                            int_searched_month = 10
                        case 'Listopad':
                            int_searched_month = 11
                        case 'Grudzień':
                            int_searched_month = 12

                    try:
                        date_selection_box_table = date_selection_box.find_element(By.CLASS_NAME, 'ui-datepicker-calendar')
                    except:
                        print('ui-datepicker-calendar not found')
                    try:
                        date_selection_box_table_body = date_selection_box_table.find_element(By.TAG_NAME, 'tbody')
                    except:
                        print('tbody not found')
                    try:
                        #data1 = date_selection_box_table_body.find_element(By.XPATH, f'//td[@data-month="' + {str(int_searched_month)} + '"]/a[text()="' + {str(searched_day)} + '"]')
                        days_list = date_selection_box_table_body.find_elements(By.CLASS_NAME, 'ui-state-default')
                        for day in days_list:
                            day_number = day.get_attribute('innerHTML').strip()
                            if str(day_number) == str(searched_day):
                                day.click()
                                time.sleep(3)
                                break
                    except:
                        print('click failed')
                    time.sleep(3)
                else:
                    #pickers = date_selection_box_header.find_elements(By.CLASS_NAME, 'ui-datepicker-prev')
                    print('current month is:' + str(current_month) + ' my month is:' + str(searched_month))
                    print('current year is:' + str(current_year) + ' my year is:' + str(searched_year))
                    try:
                        move_to_next_month_button.click()
                    except:
                        print('arrow button not found')
                    time.sleep(3)
        else:
            print(33)

    #passenger block
    try:
        passenger_number_div = form_box.find_element(By.CLASS_NAME, 'right-data')
        passenger_number_selctor = passenger_number_div.find_element(By.CLASS_NAME, 'trip-paxes')
        passenger_number_selctor.click()
        time.sleep(3)
    except:
        print('passenger number div not found')

    passenger_types_dropdown_list = driver.find_element(By.CLASS_NAME, 'pax-counter')
    #Adults numbers
    try:
        adult_number = passenger_types_dropdown_list.find_element(By.CLASS_NAME, 'adult')
    except:
        print('adult class not found')
    check = 0
    while check == 0:
        try:
            current_number = adult_number.find_element(By.CLASS_NAME, 'pax-number')
            current_number = current_number.get_attribute('innerHTML').strip()
        except:
            print('adult pax not found')
        if int(current_number) < int(adults_amount):
            try:
                current_number_increment = adult_number.find_element(By.CLASS_NAME, 'plus')
            except:
                print('increment not found')
            try:
                current_number_increment.click()
            except:
                print('increment not clicked')
            time.sleep(3)
        else:
            check = 1

    #Youth numbers
    try:
        youth_number = passenger_types_dropdown_list.find_element(By.CLASS_NAME, 'youth')
        check = 0
        while check == 0:
            current_number = youth_number.find_element(By.CLASS_NAME, 'pax-number')
            current_number = current_number.get_attribute('innerHTML').strip()
            if int(current_number) < int(youth_amount):
                current_number_increment = youth_number.find_element(By.CLASS_NAME, 'plus')
                current_number_increment.click()
                time.sleep(3)
            else:
                check = 1
    except:
        print('youth passenger counter not found')

    #Child numbers
    try:
        child_number = passenger_types_dropdown_list.find_element(By.CLASS_NAME, 'child')
        check = 0
        while check == 0:
            current_number = child_number.find_element(By.CLASS_NAME, 'pax-number')
            current_number = current_number.get_attribute('innerHTML').strip()
            if int(current_number) < int(child_amount):
                current_number_increment = child_number.find_element(By.CLASS_NAME, 'plus')
                current_number_increment.click()
                time.sleep(3)
            else:
                check = 1
    except:
        print('child passenger counter not found')

    #Babies numbers
    try:
        baby_number = passenger_types_dropdown_list.find_element(By.CLASS_NAME, 'infant')
        check = 0
        while check == 0:
            current_number = baby_number.find_element(By.CLASS_NAME, 'pax-number')
            current_number = current_number.get_attribute('innerHTML').strip()
            if int(current_number) < int(baby_amount):
                current_number_increment = baby_number.find_element(By.CLASS_NAME, 'plus')
                current_number_increment.click()
                time.sleep(3)
            else:
                check = 1
    except:
        print('baby passenger counter not found')

    #click form
    try:
        button_gotowe = passenger_types_dropdown_list.find_element(By.CLASS_NAME, 'close-pax-counter')
    except:
        print('close-pax-counter not found')
    try:
        button_gotowe.click()
    except:
        print('failed to click Gotowe button')

    #wyszukujemy lot
    try:
        #search_button_outer_box = form_box.find_element(By.CLASS_NAME, 'close-pax-counter')
        search_button = passenger_number_div.find_element(By.CLASS_NAME, 'transaction')
    except:
        print('transaction not found')
    try:
        button_name = search_button.find_element(By.CLASS_NAME, 'text')
        button_name = button_name.get_attribute('innerHTML').strip()
    except:
        print('no button name found in form')

    if button_name == 'Szukaj lotu':
        try:
            search_button.click()
            time.sleep(3)
        except:
            print('failed to click button')
    else:
        print(button_name)

    counter = counter + 1
    #Wykonujemy print screen
    try:
        driver.save_screenshot('screenshot'+ str(counter) + '.jpg')
    except:
        print('failed to save a screenshot')
    driver.quit()


