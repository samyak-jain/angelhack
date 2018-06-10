package com.example.samtan.hyp_app;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.GeolocationPermissions;
import android.webkit.WebChromeClient;

import com.hypertrack.lib.HyperTrack;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Check for Location permission
        HyperTrack.requestPermissions(this);

        HyperTrack.requestLocationServices(this);
        HyperTrack.initialize(this, "pk_6066ab2346bf020175210303a6bb8dd04071dc14");

        WebView myWebView = (WebView) findViewById(R.id.webview);
        WebSettings webSettings = myWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setGeolocationEnabled(true);
        webSettings.setJavaScriptCanOpenWindowsAutomatically(true);
        myWebView.setWebChromeClient(new WebChromeClient() {
            public void onGeolocationPermissionsShowPrompt(String origin, GeolocationPermissions.Callback callback) {
                callback.invoke(origin, true, false);
            }
        });
        myWebView.loadUrl("https://unsting-volunteer.netlify.com");


    }
}
