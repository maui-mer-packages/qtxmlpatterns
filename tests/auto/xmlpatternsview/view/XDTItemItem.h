/****************************************************************************
**
** Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
** All rights reserved.
** Contact: Nokia Corporation (qt-info@nokia.com)
**
** This file is part of the test suite of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** GNU Lesser General Public License Usage
** This file may be used under the terms of the GNU Lesser General Public
** License version 2.1 as published by the Free Software Foundation and
** appearing in the file LICENSE.LGPL included in the packaging of this
** file. Please review the following information to ensure the GNU Lesser
** General Public License version 2.1 requirements will be met:
** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** In addition, as a special exception, Nokia gives you certain additional
** rights. These rights are described in the Nokia Qt LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU General
** Public License version 3.0 as published by the Free Software Foundation
** and appearing in the file LICENSE.GPL included in the packaging of this
** file. Please review the following information to ensure the GNU General
** Public License version 3.0 requirements will be met:
** http://www.gnu.org/copyleft/gpl.html.
**
** Other Usage
** Alternatively, this file may be used in accordance with the terms and
** conditions contained in a signed written agreement between you and Nokia.
**
**
**
**
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef PatternistSDK_XDTItemItem_H
#define PatternistSDK_XDTItemItem_H

#include <QList>
#include "qitem_p.h"

#include "TreeItem.h"

QT_BEGIN_HEADER

QT_BEGIN_NAMESPACE

namespace QPatternistSDK
{
    /**
     * @short Proxies an QPatternist::Item through the TreeItem
     * interface such that Patternist data can be used in Qt's model/view
     * framework.
     *
     * @ingroup PatternistSDK
     * @author Frans Englich <frans.englich@nokia.com>
     */
    class XDTItemItem : public TreeItem
    {
    public:
        XDTItemItem(const QPatternist::Item &item,
                    XDTItemItem *parent);
        virtual ~XDTItemItem();

        virtual QVariant data(const Qt::ItemDataRole role, int column) const;

        virtual void appendChild(TreeItem *item);
        virtual TreeItem *child(const unsigned int row) const;
        virtual unsigned int childCount() const;
        virtual TreeItem::List children() const;
        virtual TreeItem *parent() const;
        int columnCount() const;

    private:
        const QPatternist::Item m_item;
        XDTItemItem *m_parent;
        TreeItem::List m_children;
    };
}

QT_END_NAMESPACE

QT_END_HEADER

#endif
// vim: et:ts=4:sw=4:sts=4
