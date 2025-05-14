from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

COUNTRIES = [
    ("AF", "Afghanistan"),
    ("AL", "Albania"),
    ("DZ", "Algeria"),
    ("AR", "Argentina"),
    ("AM", "Armenia"),
    ("AU", "Australia"),
    ("AT", "Austria"),
    ("AZ", "Azerbaijan"),
    ("BH", "Bahrain"),
    ("BD", "Bangladesh"),
    ("BY", "Belarus"),
    ("BE", "Belgium"),
    ("BZ", "Belize"),
    ("BJ", "Benin"),
    ("BT", "Bhutan"),
    ("BO", "Bolivia"),
    ("BA", "Bosnia and Herzegovina"),
    ("BW", "Botswana"),
    ("BR", "Brazil"),
    ("BN", "Brunei"),
    ("BG", "Bulgaria"),
    ("BF", "Burkina Faso"),
    ("BI", "Burundi"),
    ("KH", "Cambodia"),
    ("CM", "Cameroon"),
    ("CA", "Canada"),
    ("CV", "Cape Verde"),
    ("CF", "Central African Republic"),
    ("TD", "Chad"),
    ("CL", "Chile"),
    ("CN", "China"),
    ("CO", "Colombia"),
    ("KM", "Comoros"),
    ("CD", "Congo (Kinshasa)"),
    ("CG", "Congo (Brazzaville)"),
    ("CR", "Costa Rica"),
    ("CI", "Côte d'Ivoire"),
    ("HR", "Croatia"),
    ("CU", "Cuba"),
    ("CY", "Cyprus"),
    ("CZ", "Czech Republic"),
    ("DK", "Denmark"),
    ("DJ", "Djibouti"),
    ("DM", "Dominica"),
    ("DO", "Dominican Republic"),
    ("EC", "Ecuador"),
    ("EG", "Egypt"),
    ("SV", "El Salvador"),
    ("GQ", "Equatorial Guinea"),
    ("ER", "Eritrea"),
    ("EE", "Estonia"),
    ("SZ", "Eswatini"),
    ("ET", "Ethiopia"),
    ("FJ", "Fiji"),
    ("FI", "Finland"),
    ("FR", "France"),
    ("GA", "Gabon"),
    ("GM", "Gambia"),
    ("GE", "Georgia"),
    ("DE", "Germany"),
    ("GH", "Ghana"),
    ("GR", "Greece"),
    ("GD", "Grenada"),
    ("GT", "Guatemala"),
    ("GN", "Guinea"),
    ("GW", "Guinea-Bissau"),
    ("GY", "Guyana"),
    ("HT", "Haiti"),
    ("HN", "Honduras"),
    ("HU", "Hungary"),
    ("IS", "Iceland"),
    ("IN", "India"),
    ("ID", "Indonesia"),
    ("IR", "Iran"),
    ("IQ", "Iraq"),
    ("IE", "Ireland"),
    ("IL", "Israel"),
    ("IT", "Italy"),
    ("JM", "Jamaica"),
    ("JP", "Japan"),
    ("JO", "Jordan"),
    ("KZ", "Kazakhstan"),
    ("KE", "Kenya"),
    ("KI", "Kiribati"),
    ("KP", "Korea, North"),
    ("KR", "Korea, South"),
    ("KW", "Kuwait"),
    ("KG", "Kyrgyzstan"),
    ("LA", "Laos"),
    ("LV", "Latvia"),
    ("LB", "Lebanon"),
    ("LS", "Lesotho"),
    ("LR", "Liberia"),
    ("LY", "Libya"),
    ("LI", "Liechtenstein"),
    ("LT", "Lithuania"),
    ("LU", "Luxembourg"),
    ("MG", "Madagascar"),
    ("MW", "Malawi"),
    ("MY", "Malaysia"),
    ("MV", "Maldives"),
    ("ML", "Mali"),
    ("MT", "Malta"),
    ("MH", "Marshall Islands"),
    ("MR", "Mauritania"),
    ("MU", "Mauritius"),
    ("MX", "Mexico"),
    ("FM", "Micronesia"),
    ("MD", "Moldova"),
    ("MC", "Monaco"),
    ("MN", "Mongolia"),
    ("ME", "Montenegro"),
    ("MA", "Morocco"),
    ("MZ", "Mozambique"),
    ("MM", "Myanmar"),
    ("NA", "Namibia"),
    ("NR", "Nauru"),
    ("NP", "Nepal"),
    ("NL", "Netherlands"),
    ("NZ", "New Zealand"),
    ("NI", "Nicaragua"),
    ("NE", "Niger"),
    ("NG", "Nigeria"),
    ("NO", "Norway"),
    ("OM", "Oman"),
    ("PK", "Pakistan"),
    ("PW", "Palau"),
    ("PA", "Panama"),
    ("PG", "Papua New Guinea"),
    ("PY", "Paraguay"),
    ("PE", "Peru"),
    ("PH", "Philippines"),
    ("PL", "Poland"),
    ("PT", "Portugal"),
    ("QA", "Qatar"),
    ("RO", "Romania"),
    ("RU", "Russia"),
    ("RW", "Rwanda"),
    ("KN", "Saint Kitts and Nevis"),
    ("LC", "Saint Lucia"),
    ("VC", "Saint Vincent and the Grenadines"),
    ("WS", "Samoa"),
    ("SM", "San Marino"),
    ("ST", "Sao Tome and Principe"),
    ("SA", "Saudi Arabia"),
    ("SN", "Senegal"),
    ("RS", "Serbia"),
    ("SC", "Seychelles"),
    ("SL", "Sierra Leone"),
    ("SG", "Singapore"),
    ("SK", "Slovakia"),
    ("SI", "Slovenia"),
    ("SB", "Solomon Islands"),
    ("SO", "Somalia"),
    ("ZA", "South Africa"),
    ("SS", "South Sudan"),
    ("ES", "Spain"),
    ("LK", "Sri Lanka"),
    ("SD", "Sudan"),
    ("SR", "Suriname"),
    ("SE", "Sweden"),
    ("CH", "Switzerland"),
    ("SY", "Syria"),
    ("TW", "Taiwan"),
    ("TJ", "Tajikistan"),
    ("TZ", "Tanzania"),
    ("TH", "Thailand"),
    ("TL", "Timor-Leste"),
    ("TG", "Togo"),
    ("TO", "Tonga"),
    ("TT", "Trinidad and Tobago"),
    ("TN", "Tunisia"),
    ("TR", "Turkey"),
    ("TM", "Turkmenistan"),
    ("TV", "Tuvalu"),
    ("UG", "Uganda"),
    ("UA", "Ukraine"),
    ("AE", "United Arab Emirates"),
    ("GB", "United Kingdom"),
    ("US", "United States"),
    ("UY", "Uruguay"),
    ("UZ", "Uzbekistan"),
    ("VU", "Vanuatu"),
    ("VA", "Vatican City"),
    ("VE", "Venezuela"),
    ("VN", "Vietnam"),
    ("YE", "Yemen"),
    ("ZM", "Zambia"),
    ("ZW", "Zimbabwe"),
]

EVENT_TYPES = [
    ("Bycicle ride", "Bycicle ride"),
    ("Skiing", "Skiing"),
    ("Cinema", "Cinema"),
    ("Videogames", "Videogames"),
    ("Co-education", "Co-education"),
    ("Theatre", "Theatre"),
    ("Walk", "Walk"),
    ("Sport", "Sport"),
    ("Jogging", "Jogging"),
    ("Restaurant", "Restaurant"),
    ("Ice skating", "Ice skating"),

]
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, null=False, blank=True, verbose_name="Username")
    #first_name
    #last_name
    #is_staff
    #is_superuser
    country = models.CharField(max_length=50, choices=COUNTRIES, null=True, blank=False, verbose_name="Country")
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    avatar = models.ImageField(null=True, blank=True, verbose_name="Profile picture")
    info = models.TextField(max_length=500, blank=True, null=True, verbose_name="Additional information")
    rep = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name="Reputation")
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

        indexes = [
            models.Index(fields=['username', 'info'])
        ]

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Event name")
    type = models.CharField(max_length=50, choices=EVENT_TYPES, null=False, blank=False, verbose_name="Event type")
    max_person = models.IntegerField(validators=[MinValueValidator(1)], null=False, blank=False, verbose_name="Maximum people")
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name="Description")
    completed = models.BooleanField(default=False, null=False, blank=False, verbose_name="Is completed")
    date = models.DateTimeField(null=True, blank=False, verbose_name="Date and time")
    slug = models.SlugField(blank=True)
    participants = models.ManyToManyField(User, related_name="joined_events")
    
    #automatically generated slug for obj
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Event {self.name} by {self.user}"
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

        indexes = [
            models.Index(fields=['name', 'description'])
        ]

class Chat(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="chats")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField(max_length=200, null=True, blank=False, verbose_name="Message text")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat for {self.event}"
    
    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"
        ordering = ['created_at']

    
