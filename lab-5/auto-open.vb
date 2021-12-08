Sub Auto_Open()
	Dim msg
	msg = MsgBox("Колонтитулы установлены", vbOKOnly, "Выполнено", Help, 2000)

	ActiveSheet.PageSetup.LeftHeader = "Тюрин Иван Николаевич"
	ActiveSheet.PageSetup.CenterHeader = "Вариант 24"
	ActiveSheet.PageSetup.RightHeader = ThisWorkbook.Name
	ActiveSheet.PageSetup.CenterFooter = Format(ThisWorkbook.BuiltinDocumentProperties("Creation Date"), "d mmmm yyyy ã., hh:mm:ss")
End Sub
