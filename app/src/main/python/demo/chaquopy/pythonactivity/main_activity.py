from demo.chaquopy.pythonactivity import R
import requests
from java import static_proxy, Override, jvoid

from android.os             import Bundle
from android.support.v7.app import AppCompatActivity


# Python activities require a static_proxy implementation
#   in order to generate a Java source file from their contents.
# All files that use static proxies must be defined @ app/build.gradle
class MainActivity (static_proxy(AppCompatActivity)):

    # Any methods that will be accessed from Java must implement
    #   @Override(java_return_type, [method_args])
    @Override(jvoid, [Bundle])
    def onCreate(self, state):
        AppCompatActivity.onCreate(self, state)
        self.setContentView(R.layout.activity_main)

        label = self.findViewById(R.id.label)
        label.setText("Prakruti is mast")


