/* -*- coding: utf-8-unix -*-
 *
 * Copyright (C) 2018 Peter Pichler, inspired by Osmo Salomaa and Rinigus
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

import QtQuick 2.0
import "platform"

Column {
    anchors.leftMargin: app.styler.themePaddingSmall
    anchors.rightMargin: app.styler.themePaddingSmall

    property string value
    property string caption

    LabelPL {
        // Value
        anchors.left: parent.left
        anchors.right: parent.right
        color: app.styler.themeHighlightColor
        font.pixelSize: app.styler.themeFontSizeHuge
        height: implicitHeight * 3 / 4  // text is always a number, we can get away without the part below baseline
        verticalAlignment: Text.AlignTop
        horizontalAlignment: Text.AlignHCenter
        text: value     // assigned by the caller
    }

    LabelPL {
        // Caption
        anchors.left: parent.left
        anchors.right: parent.right
        color: app.styler.themeHighlightColor
        font.pixelSize: app.styler.themeFontSizeMedium
        verticalAlignment: Text.AlignBottom
        horizontalAlignment: Text.AlignHCenter
        text: caption   // assigned by the caller
    }
}
