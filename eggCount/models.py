from django.db import models

class rooms(models.Model):
    roomNo = models.IntegerField(unique=True)
    ChickensNo = models.IntegerField(default=0)

    ACTIVE = 'active'
    INACTIVE = 'inactive'
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('Inactive', 'inactive') 
    ]
    room_status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Active')
    def __str__(self):
        return f"rooms {self.roomNo}"
    
class eggHatch(models.Model):
    room = models.ForeignKey(rooms, null=True, on_delete=models.SET_NULL, related_name="hatches")
    eggsNo = models.IntegerField(default=0, blank=True)
    brokenEggs = models.IntegerField(default=0)
    period = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=300, default="null")


# Create your models here.
