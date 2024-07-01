import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QVBoxLayout, QWidget, QTextEdit, QPushButton, QHBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Mandakani")
        self.setGeometry(100, 100, 900, 800)
        
        # Create menu bar
        self.create_menu()

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create top frame
        top_frame = QFrame()
        top_layout = QHBoxLayout(top_frame)
        layout.addWidget(top_frame)

        # Create left and right boxes
        left_box = QFrame()
        left_box.setFrameShape(QFrame.Box)
        left_box.setFrameShadow(QFrame.Sunken)
        left_box.setFixedWidth(450)
        left_box.setFixedHeight(600)
        left_layout = QVBoxLayout(left_box)
        top_layout.addWidget(left_box)
        
        right_box = QFrame()
        right_box.setFrameShape(QFrame.Box)
        right_box.setFrameShadow(QFrame.Sunken)
        right_box.setFixedWidth(450)
        right_box.setFixedHeight(600)
        right_layout = QVBoxLayout(right_box)
        top_layout.addWidget(right_box)
        
        # Create console frame
        console_frame = QFrame()
        console_layout = QVBoxLayout(console_frame)
        layout.addWidget(console_frame)
        
        # Create console text widget
        self.console_text = QTextEdit()
        self.console_text.setReadOnly(True)
        console_layout.addWidget(self.console_text)
        
        # Add profile icon
        profile_icon = QLabel()
        profile_pixmap = QPixmap("c:/Users/winne/Desktop/DID INTERN/CDAC/Project 2/Code/Python tkinter/Login/logo.png")
        profile_pixmap = profile_pixmap.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        profile_icon.setPixmap(profile_pixmap)
        profile_icon.setAlignment(Qt.AlignRight | Qt.AlignTop)
        top_layout.addWidget(profile_icon)
        
        # Add buttons to boxes
        btn_left = QPushButton("Add to Console from Left Box")
        btn_left.clicked.connect(lambda: self.add_to_console("Message from Left Box"))
        left_layout.addWidget(btn_left, alignment=Qt.AlignTop)
        
        btn_right = QPushButton("Add to Console from Right Box")
        btn_right.clicked.connect(lambda: self.add_to_console("Message from Right Box"))
        right_layout.addWidget(btn_right, alignment=Qt.AlignTop)

    def create_menu(self):
        main_menu = self.menuBar()

        file_menu = main_menu.addMenu('File')
        edit_menu = main_menu.addMenu('Edit')
        view_menu = main_menu.addMenu('View')
        generate_menu = main_menu.addMenu('Generate')
        export_menu = main_menu.addMenu('Export')
        help_menu = main_menu.addMenu('Help')
        
        # File menu actions
        new_text_file_action = QAction('New Text File', self)
        new_file_action = QAction('New File', self)
        new_window_action = QAction('New Window', self)
        open_file_action = QAction('Open File', self)
        open_folder_action = QAction('Open Folder', self)
        open_workspace_action = QAction('Open Workspace from File', self)
        open_recent_action = QAction('Open Recent', self)
        add_folder_action = QAction('Add Folder to Workspace', self)
        save_workspace_as_action = QAction('Save Workspace As', self)
        duplicate_workspace_action = QAction('Duplicate Workspace', self)
        save_action = QAction('Save', self)
        save_as_action = QAction('Save As', self)
        save_all_action = QAction('Save All', self)
        auto_save_action = QAction('Auto Save', self)
        print_action = QAction('Print', self)
        share_action = QAction('Share', self)
        revert_file_action = QAction('Revert File', self)
        close_folder_action = QAction('Close Folder', self)
        close_window_action = QAction('Close Window', self)
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)

        # Add actions to File menu
        file_menu.addAction(new_text_file_action)
        file_menu.addAction(new_file_action)
        file_menu.addAction(new_window_action)
        file_menu.addSeparator()
        file_menu.addAction(open_file_action)
        file_menu.addAction(open_folder_action)
        file_menu.addAction(open_workspace_action)
        file_menu.addAction(open_recent_action)
        file_menu.addSeparator()
        file_menu.addAction(add_folder_action)
        file_menu.addAction(save_workspace_as_action)
        file_menu.addAction(duplicate_workspace_action)
        file_menu.addSeparator()
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(save_all_action)
        file_menu.addAction(auto_save_action)
        file_menu.addAction(print_action)
        file_menu.addSeparator()
        file_menu.addAction(share_action)
        file_menu.addSeparator()
        file_menu.addAction(revert_file_action)
        file_menu.addAction(close_folder_action)
        file_menu.addAction(close_window_action)
        file_menu.addAction(exit_action)

        # Edit menu actions
        undo_action = QAction('Undo', self)
        redo_action = QAction('Redo', self)
        cut_action = QAction('Cut', self)
        copy_action = QAction('Copy', self)
        paste_action = QAction('Paste', self)
        find_action = QAction('Find', self)
        replace_action = QAction('Replace', self)
        find_in_files_action = QAction('Find in Files', self)
        replace_in_files_action = QAction('Replace in Files', self)

        # Add actions to Edit menu
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addSeparator()
        edit_menu.addAction(find_action)
        edit_menu.addAction(replace_action)
        edit_menu.addSeparator()
        edit_menu.addAction(find_in_files_action)
        edit_menu.addAction(replace_in_files_action)

        # View menu actions
        open_view_action = QAction('Open View', self)
        appearance_action = QAction('Appearance', self)
        editor_layout_action = QAction('Editor Layout', self)
        explorer_action = QAction('Explorer', self)
        search_action = QAction('Search', self)
        source_control_action = QAction('Source Control', self)
        run_action = QAction('Run', self)
        extensions_action = QAction('Extensions', self)
        problems_action = QAction('Problems', self)
        output_action = QAction('Output', self)
        word_wrap_action = QAction('Word Wrap', self)

        # Add actions to View menu
        view_menu.addAction(open_view_action)
        view_menu.addSeparator()
        view_menu.addAction(appearance_action)
        view_menu.addAction(editor_layout_action)
        view_menu.addSeparator()
        view_menu.addAction(explorer_action)
        view_menu.addAction(search_action)
        view_menu.addAction(source_control_action)
        view_menu.addAction(run_action)
        view_menu.addAction(extensions_action)
        view_menu.addSeparator()
        view_menu.addAction(problems_action)
        view_menu.addAction(output_action)
        view_menu.addSeparator()
        view_menu.addAction(word_wrap_action)

        # Generate menu action
        generate_file_action = QAction('Generate File', self)
        generate_menu.addAction(generate_file_action)

        # Export menu action
        export_file_action = QAction('Export File', self)
        export_menu.addAction(export_file_action)

        # Help menu actions
        welcome_action = QAction('Welcome', self)
        show_all_commands_action = QAction('Show All Commands', self)
        documentation_action = QAction('Documentation', self)
        show_release_notes_action = QAction('Show Release Notes', self)
        keyboard_shortcut_action = QAction('Keyboard Shortcut Reference', self)
        video_tutorials_action = QAction('Video Tutorials', self)
        tips_and_tricks_action = QAction('Tips and Tricks', self)
        join_us_on_youtube_action = QAction('Join Us on YouTube', self)
        search_feature_requests_action = QAction('Search Feature Requests', self)
        report_issue_action = QAction('Report Issue', self)
        view_license_action = QAction('View License', self)
        privacy_statement_action = QAction('Privacy Statement', self)
        check_for_updates_action = QAction('Check for Updates', self)
        about_action = QAction('About', self)

        # Add actions to Help menu
        help_menu.addAction(welcome_action)
        help_menu.addSeparator()
        help_menu.addAction(show_all_commands_action)
        help_menu.addAction(documentation_action)
        help_menu.addAction(show_release_notes_action)
        help_menu.addSeparator()
        help_menu.addAction(keyboard_shortcut_action)
        help_menu.addAction(video_tutorials_action)
        help_menu.addAction(tips_and_tricks_action)
        help_menu.addSeparator()
        help_menu.addAction(join_us_on_youtube_action)
        help_menu.addAction(search_feature_requests_action)
        help_menu.addAction(report_issue_action)
        help_menu.addSeparator()
        help_menu.addAction(view_license_action)
        help_menu.addAction(privacy_statement_action)
        help_menu.addSeparator()
        help_menu.addAction(check_for_updates_action)
        help_menu.addSeparator()
        help_menu.addAction(about_action)

    def add_to_console(self, message):
        self.console_text.append(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
