aqi_state = hass.states.get('sensor.waqi_salt_lake_city_utah').state
aqi_state = int(aqi_state)

if aqi_state < 50:
    color = 'green'
    health_implications = 'Air quality is considered satisfactory, and air pollution poses little or no risk'
    cautionary_statement = 'None'
    picture = '/local/images/cloud-green.png'
elif aqi_state < 100:
    color = 'yellow'
    health_implications = 'Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
    cautionary_statement = 'Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion.'
    picture = '/local/images/cloud-yellow.png'
elif aqi_state < 150:
    color = 'orange'
    health_implications = 'Members of sensitive groups may experience health effects. The general public is not likely to be affected.'
    cautionary_statement = 'Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion.'
    picture = '/local/images/cloud-orange.png'
elif aqi_state < 200:
    color = 'red'
    health_implications = 'Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects'
    cautionary_statement = 'Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion'
    picture = '/local/images/cloud-red.png'
elif aqi_state < 300:
    color = 'purple'
    health_implications = 'Health warnings of emergency conditions. The entire population is more likely to be affected.'
    cautionary_statement = 'Active children and adults, and people with respiratory disease, such as asthma, should avoid all outdoor exertion; everyone else, especially children, should limit outdoor exertion.'
    picture = '/local/images/cloud-purple.png'
elif aqi_state > 300:
    color = 'black'
    health_implications = 'Health alert: everyone may experience more serious health effects'
    cautionary_statement = 'Everyone should avoid all outdoor exertion'
    picture = '/local/images/cloud-black.png'


hass.states.set('sensor.aqi', color, {
    #'icon':'mdi:cloud-outline',
    'entity_picture':picture,
    'friendly_name': 'AQI',
    'health_implications': health_implications,
    'cautionary_statement': cautionary_statement
    })

