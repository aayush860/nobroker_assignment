from selenium.webdriver.common.by import By


class login_page_locators(object):
    # --------------- Clear_permissions
    clear_permissions = ['com.nobroker.app:id/bottomPermission',  # click_continue
                         'com.android.permissioncontroller:id/permission_allow_button',  # allow_to_make_phone_call
                         'com.android.permissioncontroller:id/permission_allow_button',  # allow_to_access_contacts
                         'com.android.permissioncontroller:id/permission_allow_always_button'
                         # allow_to_access_permission_all_the_time
                         ]

    # --------------- Page 1 to goto bangalore location
    search_guide = ['com.nobroker.app:id/buyLayoutText',  # click_on_buy_button
                    'com.nobroker.app:id/locationImageHome',  # click_for_bangalore_default
                    ]
    search_field = 'com.nobroker.app:id/localityAutoCompleteTxt'
    searched_click = 'com.nobroker.app:id/logo'

    # --------------- Searching property and navigation to next page
    include_nearby_property = 'com.nobroker.app:id/nearByRadio'
    two_bhk = 'com.nobroker.app:id/bhktwo'
    three_bhk = 'com.nobroker.app:id/bhkthree'
    search_property = 'com.nobroker.app:id/searchProperty'
    search_params = [include_nearby_property, two_bhk, three_bhk, search_property, search_property]




