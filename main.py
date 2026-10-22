import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import pyperclip

kivy.require('2.3.0')

class ClipboardManagerApp(App):
    def build(self):
        self.title = "Smart Clipboard & Notes"
        self.history = []

        # Root layout
        root = BoxLayout(orientation='vertical', padding=18, spacing=12)

        # Header Title
        title_label = Label(
            text="📱 Mobile Clipboard Hub",
            font_size='22sp',
            size_hint_y=None,
            height=45,
            bold=True
        )
        root.add_widget(title_label)

        # Text input field
        self.text_input = TextInput(
            text="Type or paste text here...",
            multiline=True,
            font_size='16sp',
            size_hint_y=0.28
        )
        root.add_widget(self.text_input)

        # Action button bar
        btn_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=48)

        copy_btn = Button(
            text="📋 Copy to Clipboard",
            background_color=(0.1, 0.65, 0.45, 1)
        )
        copy_btn.bind(on_press=self.copy_action)
        btn_layout.add_widget(copy_btn)

        paste_btn = Button(
            text="📥 Paste from Clipboard",
            background_color=(0.2, 0.5, 0.85, 1)
        )
        paste_btn.bind(on_press=self.paste_action)
        btn_layout.add_widget(paste_btn)

        clear_btn = Button(
            text="✖ Clear",
            size_hint_x=0.3,
            background_color=(0.7, 0.2, 0.2, 1)
        )
        clear_btn.bind(on_press=self.clear_action)
        btn_layout.add_widget(clear_btn)

        root.add_widget(btn_layout)

        # Status message
        self.status_label = Label(
            text="Ready. Tap 'Copy to Clipboard' or 'Paste'.",
            font_size='13sp',
            size_hint_y=None,
            height=30,
            color=(0.7, 0.8, 0.9, 1)
        )
        root.add_widget(self.status_label)

        # History Header
        history_title = Label(
            text="Recent Saved Clips",
            font_size='16sp',
            bold=True,
            size_hint_y=None,
            height=32
        )
        root.add_widget(history_title)

        # Scrollable list of recent clips
        scroll = ScrollView(size_hint=(1, 0.45))
        self.history_grid = GridLayout(cols=1, spacing=8, size_hint_y=None)
        self.history_grid.bind(minimum_height=self.history_grid.setter('height'))
        scroll.add_widget(self.history_grid)
        root.add_widget(scroll)

        return root

    def copy_action(self, instance):
        content = self.text_input.text.strip()
        if content:
            pyperclip.copy(content)
            self.status_label.text = f"✓ Copied {len(content)} chars to clipboard!"
            self.add_history(content)
        else:
            self.status_label.text = "⚠️ Input is empty. Nothing to copy."

    def paste_action(self, instance):
        try:
            pasted = pyperclip.paste()
            if pasted:
                self.text_input.text = pasted
                self.status_label.text = "✓ Pasted text from mobile clipboard!"
            else:
                self.status_label.text = "Clipboard is currently empty."
        except Exception as e:
            self.status_label.text = f"Paste error: {str(e)}"

    def clear_action(self, instance):
        self.text_input.text = ""
        self.status_label.text = "Cleared text input."

    def add_history(self, text):
        if text not in self.history:
            self.history.insert(0, text)
            item_btn = Button(
                text=text[:35] + ("..." if len(text) > 35 else ""),
                size_hint_y=None,
                height=42,
                background_color=(0.25, 0.3, 0.4, 0.9)
            )
            item_btn.bind(on_press=lambda b: self.select_clip(text))
            self.history_grid.add_widget(item_btn)

    def select_clip(self, text):
        self.text_input.text = text
        self.status_label.text = "Loaded clip into editor."

if __name__ == '__main__':
    ClipboardManagerApp().run()
