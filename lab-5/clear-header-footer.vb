Sub ClearHeaderAndFooter()

	' Объявление переменных
	Dim msg
	msg = MsgBox("Колонтитулы очищены", vbOKOnly, "Выполнено", Help, 2000)
	
	' Очистка колонтитулов
	ActiveSheet.PageSetup.LeftHeader = ""
	ActiveSheet.PageSetup.CenterHeader = ""
	ActiveSheet.PageSetup.RightHeader = ""
	ActiveSheet.PageSetup.LeftFooter = ""
	ActiveSheet.PageSetup.CenterFooter = ""
	ActiveSheet.PageSetup.RightFooter = ""

End Sub
